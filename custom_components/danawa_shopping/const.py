"""Constants for the Detailed Hello World Push integration."""
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

# This is the internal name of the integration, it should also match the directory
# name for the integration.
DOMAIN = "danawa_shopping"
NAME = "Danawa Shopping"
VERSION = "1.0.0"

CONF_OPTION_MODIFY = "option_modify"
CONF_OPTION_ADD = "option_add"
CONF_OPTION_SELECT = "option_select"
CONF_OPTION_DELETE = "option_delete"
CONF_OPTION_ENTITIES = "option_entities"

CONF_OPTIONS = [
    CONF_OPTION_MODIFY,
    CONF_OPTION_ADD
]

CONF_SEARCH_KEYWORD = "search_keyword"
CONF_KEYWORDS = "keywords"
CONF_WORD = "word"
CONF_REFRESH_PERIOD = "refresh_period"
CONF_SORT_TYPE = "sort_type"

CONF_FILTER = "filter"

FILTER_TYPES = {
    "쿠팡와우할인": "CoupangMemberSort",
    "배송비포함": "addDelivery"
}

FILTER_TYPES_REVERSE = {
    "CoupangMemberSort": "쿠팡와우할인",
    "addDelivery": "배송비포함",
}

SORT_TYPES = {
    "인기상품순": "saveDESC",
    "신상품순": "dateDESC",
    "낮은가격순": "priceASC",
    "높은가격순": "priceDESC",
    "상품의견많은순": "opinionDESC"
}

SORT_TYPES_REVERSE = {
    "saveDESC": "인기상품순",
    "dateDESC": "신상품순",
    "priceASC": "낮은가격순",
    "priceDESC": "높은가격순",
    "opinionDESC": "상품의견많은순"
}

CONF_URL = "https://search.danawa.com/dsearch.php?query="

REFRESH_MIN = 60
