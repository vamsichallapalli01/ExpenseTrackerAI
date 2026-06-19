var staticCacheName = "expense-tracker-ai-v4";

var filesToCache = [
    '/login/',
    '/manifest.json',
    '/static/icon-160.png',
    '/static/icon-512.png'
];

self.addEventListener("install", event => {
    self.skipWaiting();

    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => cache.addAll(filesToCache))
    );
});

self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== staticCacheName) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => response || fetch(event.request))
    );
});