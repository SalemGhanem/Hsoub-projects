const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('blog.db', (err) => {
    if (err) {
        return console.error(err.message);
    }
    console.log('Connected to the Blog SQLite database');
});
/*
db.run('CREATE TABLE Articles(ArticleID INTEGER PRIMARY KEY, ArticleName TEXT, Author TEXT, Date TEXT)', function(err) {
    if (err) {
        return console.log(err.message);
    }
    console.log('Table One Created');
});

db.run('CREATE TABLE Comments(CommentID INTEGER PRIMARY KEY, Name TEXT, Content TEXT, Date TEXT, ArticleID INTEGER, FOREIGN KEY (ArticleID) REFERENCES Articles(ArticleID))', function(err) {
    if (err) {
        return console.log(err.message);
    }
    console.log('Table Two Created');
});
*/

db.run(
    'INSERT INTO Articles (ArticleID, ArticleName, Date) VALUES (111, "php", "2020"), (112, "C#", "2024")',
    function (err) {
      if (err) {
        return console.error(err.message);
      }
      console.log('Data inserted into Articles Table');
    }
  );
  


db.close((err) => {
    if (err) {
        return console.error(err.message);
    }
    console.log('Close the database connection.');
});
