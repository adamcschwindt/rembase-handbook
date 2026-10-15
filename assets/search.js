// Simple search over the handbook. The index is built by build.py (search-index.js).
(function () {
  var q = document.getElementById('q');
  var box = document.getElementById('results');
  if (!q || !box || !window.RB_INDEX) return;

  function esc(s) {
    return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }
  function snippet(text, words) {
    var low = text.toLowerCase(), at = -1;
    for (var i = 0; i < words.length && at < 0; i++) at = low.indexOf(words[i]);
    var start = Math.max(0, at - 50), s = (start > 0 ? '… ' : '') + text.slice(start, start + 160) + '…';
    s = esc(s);
    words.forEach(function (w) {
      if (w.length > 1) s = s.replace(new RegExp('(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi'), '<mark>$1</mark>');
    });
    return s;
  }
  function run() {
    var words = q.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    if (!words.length) { box.hidden = true; box.innerHTML = ''; return; }
    var hits = window.RB_INDEX.map(function (it) {
      var hay = (it.chapter + ' ' + it.section + ' ' + it.text).toLowerCase(), score = 0;
      for (var i = 0; i < words.length; i++) {
        if (hay.indexOf(words[i]) < 0) return null;
        if ((it.section + ' ' + it.chapter).toLowerCase().indexOf(words[i]) >= 0) score += 3;
        score += 1;
      }
      return { it: it, score: score };
    }).filter(Boolean).sort(function (a, b) { return b.score - a.score; }).slice(0, 12);
    box.hidden = false;
    box.innerHTML = hits.length ? hits.map(function (h) {
      var it = h.it;
      return '<a href="' + it.page + (it.anchor ? '#' + it.anchor : '') + '"><div class="r-t">' + esc(it.chapter) +
        (it.section !== it.chapter ? ' › ' + esc(it.section) : '') + '</div><div class="r-s">' + snippet(it.text, words) + '</div></a>';
    }).join('') : '<div class="none">Nothing found. Try another word, or ask Becca.</div>';
  }
  q.addEventListener('input', run);
})();
