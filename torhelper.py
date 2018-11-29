from resources.lib import tor

class TorFeeds:
    def __init__(self):
        self.feeds = []
        self.time = 0
        
    def add_feeds(self, feeds):
        '''
        Add an array of feeds
        '''
        self.feeds = feeds
        
    def add_feed(self, feed):
        torFeed = TorFeed(feed)
        self.feeds.append(torFeed)
        
    def get_feeds(self):
        result = []
        for tFeed in self.feeds:
            result.append(tFeed.feed)
        return result
    def serialize(self):
        feeds = []
        for feed in self.feeds:
            feeds.append( feed.serialize())
            
        output = {
            "time": self.time,
            "feeds" : feeds
        }
        return repr(output)
    
    def unserialize(self, object):
        self.time = object["time"]
        for oFeed in object["feeds"]:
            feed = TorFeed(None)
            feed.unserialize(oFeed)
            self.add_feed(feed.feed)
    
    def __getstate__(self):
        d = dict(self.__dict__)
        del d['feeds']
        return d
    
    def __setstate__(self, d):
        self.__dict__.update(d)

class TorFeed:
    def __init__(self, feed):
        self.feed = tor.Subscriptions(None)
        self.feed = feed
    
    def serialize(self):
        
        output = {
            "feed":{
                "id":               self.feed.id,
                "matches":          self.feed.matches,
                "title":            self.feed.title,
                "iconUrl":          self.feed.iconUrl,
                "firstitemmsec":    self.feed.firstitemmsec,
                "unread_count":     self.feed.unread_count
            }
        }
        return output
    
    def unserialize(self, object):
        self.feed = tor.Subscriptions(None)
        self.feed.id =              object["feed"]["id"]
        self.feed.matches =         object["feed"]["matches"]
        self.feed.title =           object["feed"]["title"]
        self.feed.iconUrl =         object["feed"]["iconUrl"]
        self.feed.firstitemmsec =   object["feed"]["firstitemmsec"]
        self.feed.unread_count =    object["feed"]["unread_count"]
        
    def __getstate__(self):
        d = dict(self.__dict__)
        #del d['_logger']
        return d
    
    def __setstate__(self, d):
        self.__dict__.update(d)
        

class TorList:
    '''
    Helps to save a feed to cache
    '''
    def __init__(self):
        self.posts = []
        self.time = 0
    
    def count(self):
        return len(self.posts)
    
    def add_post(self, post):
        self.posts.append(post)
        self.posts = sorted(self.posts, key=lambda TorPost: TorPost.item.published, reverse=True)
    
    def get_post_list(self):
        '''
        result = []
        for post in self.posts:
            result.append(post.item.title)
        return result
        '''
        return self.posts
    
    def serialize(self):
        posts = []
        for post in self.posts:
            posts.append( post.serialize())
            
        output = {
            "time": self.time,
            "posts" : posts
        }
        
        return repr(output)
    
    def unserialize(self, object):
        self.time = object["time"]
        for oPost in object["posts"]:
            post = TorPost(None)
            post.unserialize(oPost)
            self.add_post(post)
            
    def __getstate__(self):
        d = dict(self.__dict__)
        del d['posts']
        return d
    
    def __setstate__(self, d):
        self.__dict__.update(d)

class TorPost:
    
    def __init__(self, item):
        self.item = item

        
    def __getstate__(self):
        d = dict(self.__dict__)
        #del d['_logger']
        return d
    
    def __setstate__(self, d):
        self.__dict__.update(d)
        
    def serialize(self):
        
        output = {
            "item":{
                "item_id": self.item.item_id,
                "title" : self.item.title,
                "content" : self.item.content,
                "href" : self.item.href,
                "mediaUrl" : self.item.mediaUrl,
                "source" : self.item.source,
                "source_id" : self.item.source_id,
                "published": self.item.published,
                #"video":        self.item.video
            }
        }
        return output
    
    def unserialize(self, object):
        self.item = tor.Item(None, object["item"]["item_id"])
        self.item.title = object["item"]["title"]
        self.item.content = object["item"]["content"]
        self.item.href = object["item"]["href"]
        self.item.mediaUrl = object["item"]["mediaUrl"]
        self.item.source = object["item"]["source"]
        self.item.source_id = object["item"]["source_id"]
        self.item.published = object["item"]["published"]
        #self.item.video = object["item"]["video"]
        
        