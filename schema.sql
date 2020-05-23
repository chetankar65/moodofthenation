CREATE TABLE headlines (
  id INTEGER PRIMARY KEY,
  headline TEXT NOT NULL
);

CREATE TABLE current (
  id INTEGER PRIMARY KEY,
  mood INTEGER NOT NULL,
  hour DATE not null
);

