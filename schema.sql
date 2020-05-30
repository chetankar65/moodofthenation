CREATE TABLE headlines (
  id INTEGER PRIMARY KEY,
  headline TEXT NOT NULL
);

CREATE TABLE current (
  id INTEGER PRIMARY KEY,
  mood INTEGER NOT NULL,
  hour DATE not null
);

--CREATE TABLE user (
--id TEXT PRIMARY KEY,
---  name TEXT NOT NULL,
---  email TEXT UNIQUE NOT NULL,
---  profile_pic TEXT NOT NULL
--);--