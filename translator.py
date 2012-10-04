import urllib2
import urllib
import json
from BeautifulSoup import BeautifulSoup

class translator:
    """
    This class uses the Beautiful Soup library to scrape the information from
    the HTML source code from Google Translate.

    It also offers a way to consume the AJAX result of the translation, however
    encoding on Windows won't work well right now so it's recommended to use
    the scraping method.
    """

    def fromHtml(self, text, languageFrom, languageTo):
        """
        Returns translated text that is scraped from Google Translate's HTML
        source code.
        """
        langCode={
            "arabic":"ar", "bengali":"bn", "bulgarian":"bg", "chinese":"zh-CN",
            "croatian":"hr", "czech":"cs", "danish":"da", "dutch":"nl",
            "english":"en", "finnish":"fi", "french":"fr", "german":"de",
            "greek":"el", "gujarati":"gu", "hindi":"hi", "italian":"it", "japanese":"ja",
            "korean":"ko", "norwegian":"no", "polish":"pl", "portugese":"pt",
            "romanian":"ro", "russian":"ru", "spanish":"es", "swedish":"sv", "tamil":"ta",
            "telugu":"te" }

        urllib.FancyURLopener.version = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008070400 SUSE/3.0.1-0.1 Firefox/3.0.1"

        try:
            postParameters = urllib.urlencode({"langpair":"%s|%s" %(langCode[languageFrom.lower()],langCode[languageTo.lower()]), "text":text,"ie":"UTF8", "oe":"UTF8"})
        except KeyError, error:
            print "Currently we do not support %s" %(error.args[0])
            return

        page = urllib.urlopen("http://translate.google.com/translate_t", postParameters)
        #content = page.read()
        #page.close()

        #htmlSource = BeautifulSoup(content)
        htmlSource = BeautifulSoup(page)
        #translation = htmlSource.find('span', title=text )
        return htmlSource.find('span', id='result_box').find('span').renderContents()
        #return translation.renderContents()

    """
       This will not work without Google permission as it requires access to the paid APIs.
    """
    def fromAjax(self, text, languageFrom, languageTo):
        """
        Returns a simple string translating the text from "languageFrom" to
        "LanguageTo" using Google Translate AJAX Service.
        """
        LANG={
            "arabic":"ar", "bulgarian":"bg", "chinese":"zh-CN",
            "croatian":"hr", "czech":"cs", "danish":"da", "dutch":"nl",
            "english":"en", "finnish":"fi", "french":"fr", "german":"de",
            "greek":"el", "hindi":"hi", "italian":"it", "japanese":"ja",
            "korean":"ko", "norwegian":"no", "polish":"pl", "portugese":"pt",
            "romanian":"ro", "russian":"ru", "spanish":"es", "swedish":"sv" }

        base_url='http://ajax.googleapis.com/ajax/services/language/translate?'
        langpair='%s|%s'%(LANG.get(languageFrom.lower(),languageFrom),
                          LANG.get(languageTo.lower(),languageTo))
        params=urllib.urlencode( (('v',1.0),
                           ('q',text.encode('utf-8')),
                           ('langpair',langpair),) )
        url=base_url+params
        content=urllib2.urlopen(url).read()
        try: trans_dict=json.loads(content)
        except AttributeError:
            try: trans_dict=json.load(content)
            except AttributeError: trans_dict=json.read(content)
        return trans_dict['responseData']['translatedText']

