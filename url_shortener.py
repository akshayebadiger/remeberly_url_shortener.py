import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.words = {
            "subjects": ["spiderman", "ironman", "batman", "superman", "cat", "dog", "elephant", "lion", "tiger", "eagle"],
            "verbs": ["loves", "hates", "eats", "chases", "defeats", "catches", "finds", "loses", "creates", "destroys"],
            "objects": ["apple", "banana", "carrot", "mouse", "thanos", "joker", "city", "world", "universe", "dream"]
        }

    def generate_slug(self):
        subject = random.choice(self.words["subjects"])
        verb = random.choice(self.words["verbs"])
        object = random.choice(self.words["objects"])
        return f"{subject}-{verb}-{object}"

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
