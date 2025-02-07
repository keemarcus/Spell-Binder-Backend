drop table if exists users;

create table users(
	user_id bigserial primary key,
	username varchar not null
);

insert into users values
	(0, 'user 0'),
	(default, 'user 1'),
	(default, 'user 2');
	