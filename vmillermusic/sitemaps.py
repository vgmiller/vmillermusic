from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "music_index",
            "music_about",
            "music_recordings",
            "music_repertoire",
            "music_samplePrograms",
            "music_news",
            "music_contact",
        ]

    def location(self, item):
        return reverse(item)
