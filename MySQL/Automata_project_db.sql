create database automata;
use automata;

create table finite_automata(
    id int auto_increment not null,
	states varchar(50) not null,
    alphabet varchar(50) not null,
    transitions varchar(100) not null,
    initial_state varchar(50) not null,
    final_states varchar(50) not null,
    primary key (id)
);