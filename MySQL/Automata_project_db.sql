create database automata;
use automata;

create table finite_automata(
	states varchar(50) not null,
    alphabet varchar(50) not null,
    transitions varchar(100) not null,
    initial_state varchar(50) not null,
    final_states varchar(50) not null
);

drop table finite_automata;
select * from finite_automata;