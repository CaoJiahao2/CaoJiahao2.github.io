(function () {
  'use strict';

  var input = document.querySelector('.search-input');
  var results = document.querySelector('#results');
  if (!input || !results) { return; }

  var index = [];
  var lastQuery = '';

  function escapeHTML(str) {
    return String(str).replace(/[&<>"']/g, function (m) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m];
    });
  }

  function loadIndex(cb) {
    if (index.length > 0) { cb(); return; }
    fetch('/search.json')
      .then(function (r) { return r.json(); })
      .then(function (data) { index = data || []; cb(); })
      .catch(function () { results.innerHTML = '<p>搜索索引加载失败，请稍后重试。</p>'; });
  }

  function render(items) {
    if (!items.length) {
      results.innerHTML = '<p>未找到相关内容。</p>';
      return;
    }
    var html = items.slice(0, 20).map(function (item) {
      var title = escapeHTML(item.title || '');
      var url = escapeHTML(item.url || '#');
      var excerpt = item.excerpt ? '<p class="archive__item-excerpt">' + escapeHTML(item.excerpt) + '</p>' : '';
      return '<div class="list__item"><article class="archive__item">' +
        '<h2 class="archive__item-title no_toc"><a href="' + url + '" rel="permalink">' + title + '</a></h2>' +
        excerpt +
        '</article></div>';
    }).join('');
    results.innerHTML = html;
  }

  function search(query) {
    if (!query) { results.innerHTML = ''; return; }
    loadIndex(function () {
      var q = query.toLowerCase();
      var scored = [];
      index.forEach(function (doc) {
        var title = String(doc.title || '').toLowerCase();
        var excerpt = String(doc.excerpt || '').toLowerCase();
        var tags = (doc.tags || []).join(' ').toLowerCase();
        var cats = (doc.categories || []).join(' ').toLowerCase();
        var haystack = title + ' ' + tags + ' ' + cats + ' ' + excerpt;
        if (haystack.indexOf(q) !== -1) {
          var score = 0;
          if (title.indexOf(q) !== -1) { score += 10; }
          if ((tags + ' ' + cats).indexOf(q) !== -1) { score += 5; }
          if (excerpt.indexOf(q) !== -1) { score += 1; }
          scored.push({ doc: doc, score: score });
        }
      });
      scored.sort(function (a, b) { return b.score - a.score; });
      render(scored.map(function (s) { return s.doc; }));
    });
  }

  var debounceTimer;
  input.addEventListener('input', function () {
    clearTimeout(debounceTimer);
    var value = input.value.trim();
    if (value === lastQuery) { return; }
    lastQuery = value;
    debounceTimer = setTimeout(function () { search(value); }, 150);
  });
})();
