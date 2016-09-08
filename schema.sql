drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	title string not null,
	text string not null
);

CREATE TABLE accounts (
	uid	INTEGER PRIMARY KEY AUTOINCREMENT,
	username	TEXT,
	password	TEXT,
	email		TEXT,
);