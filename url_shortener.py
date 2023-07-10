import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.themes = {
            "marvel": ["ironman", "thor", "hulk", "blackwidow", "captainamerica"],
            "hollywood": ["star", "cinema", "director", "script", "scene"],
            "elements": ["hydrogen", "helium", "lithium", "beryllium", "boron"],
            "animals": ["lion", "tiger", "elephant", "giraffe", "panda"],
            "fruits": ["apple", "banana", "cherry", "date", "elderberry"]
        }

    def generate_slug(self, theme):
        words = self.themes.get(theme, ["key", "lime", "pie"])
        word1 = random.choice(words)
        word2 = random.choice(words)
        word3 = random.choice(words)
        return f"{word1}-{word2}-{word3}"

    def shorten_url(self, long_url, theme=None):
        # Ensure we generate a unique slug
        while True:
            slug = self.generate_slug(theme)
            if slug not in self.url_mapping:
                break
        self.url_mapping[slug] = long_url
        return f"remember.ly/{slug}"

    def get_long_url(self, short_url):
        slug = short_url.replace("remember.ly/", "")
        return self.url_mapping.get(slug, "")
