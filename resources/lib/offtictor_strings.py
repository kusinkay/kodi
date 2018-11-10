class OffticTorStrings:
    def __init__(self, addon):
        self.addon = addon
        self.strs = {
            "General":                      32001,
            "Login":                        32011,
            "Password":                     32012,
            "Connected":                    32013,
            "Mark_as_read":                 32014,
            "Mark_as_unread":               32015,
            "Play_with_Youtube":            32016,
            "Marked_as_read":               32017,
            "Marked_as_unread":             32018,
            "Can_not_mark_as_read":         32019,
            "Can_not_mark_as_unread":       32020,
            "List_subcriptions":            32021,
            "Clear_cache":                  32022,
            "Cache_cleared":                32023,
            "Behaviour":                    32024,
            "Max_feed_len":                 32025,
            "Subscriptions_preloaded":      32026,
            "Next_page":                    32027,
            "Loading_subscriptions":        32028,
            "Progress_title":               32029,
            "Regular_blogs":                32030,
            "Podcast_blogs":                32031,
            "Feed_matches":                 32032,
            "No_feed_matches":              32033,
            
            "Can_not_connect":              33001,
            "Can_not_connect_TOR":          33002,
            "Can_not_start":                33003,
            
        }
        
    def get(self, string):
       
       code = self.strs[string] 
       st = self.addon.getLocalizedString(code).encode("utf-8")
        
       return st