from slyguy.language import BaseLanguage

class Language(BaseLanguage):
    BEST_OF          = 30001

    LOGIN_ERROR      = 30003
    CHANNELS         = 30004
    FEATURED         = 30005
    NO_DATA          = 30006
    WHATS_ON         = 30007
    SPORTS           = 30008
    LIVE             = 30009
    DATE_FORMAT      = 30010
    NO_ASSET_ERROR   = 30011
    NO_MPD_ERROR     = 30012
    NO_ENTITLEMENT   = 30013
    TOKEN_ERROR      = 30014
    FREEMIUM         = 30015

_ = Language()
