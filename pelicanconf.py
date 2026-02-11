AUTHOR = 'sayo'
SITENAME = 'sayo'
SITELOGO = 'https://raw.githubusercontent.com/gravelrodnova/gravelrodnova.github.io/refs/heads/main/content/images/Novas_oc_with_smoke.jpg'
SITEDESCRIPTION = 'personal site, possibly a blog'

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

DISPLAY_HOME = False

DARK_LIGHT_SWITCHING_OFF = False

USE_FOLDER_AS_CATEGORY = False
PATH_METADATA = r"(?P<path_no_ext>.*)\..*"
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = "{path_no_ext}.html"