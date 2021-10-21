const randomWordWikipedia = require('random-word-wikipedia');
randomWordWikipedia().then(console.log);
//=> [ 'Saxifraga spathularis' ]
randomWordWikipedia('ja',1).then(console.log);