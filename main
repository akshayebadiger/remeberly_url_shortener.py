import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.words = [
            "key", "lime", "pie", "fun", "joy", "run", "jump", "play", "sky", "star", 
            "moon", "sun", "light", "dark", "rain", "cloud", "tree", "leaf", "bird", "song",
            "heart", "love", "laugh", "smile", "dance", "music", "book", "dream", "cake", "sweet",
            "ice", "snow", "wind", "fire", "water", "mountain", "river", "ocean", "flower", "grass",
            "cat", "dog", "mouse", "cheese", "fruit", "cherry", "berry", "apple", "orange", "banana"
        ]

    def generate_slug(self):
        word1 = random.choice(self.words)
        word2 = random.choice(self.words)
        word3 = random.choice(self.words)
        return f"{word1}-{word2}-{word3}"

    def shorten_url(self, long_url):
        # Ensure we generate a unique slug
        while True:
            slug = self.generate_slug()
            if slug not in self.url_mapping:
                break
        self.url_mapping[slug] = long_url
        return f"remember.ly/{slug}"

    def get_long_url(self, short_url):
        slug = short_url.replace("remember.ly/", "")
        return self.url_mapping.get(slug, "")
