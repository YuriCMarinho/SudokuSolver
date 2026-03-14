:- use_module(library(clpfd)).

sudoku(Linhas) :-
    length(Linhas, 9),
    maplist(same_length(Linhas), Linhas),
    append(Linhas, Valores), Valores ins 1..9,

    maplist(all_distinct, Linhas),
    transpose(Linhas, Colunas),
    maplist(all_distinct, Colunas),

    Linhas = [L1,L2,L3,L4,L5,L6,L7,L8,L9],
    blocos(L1,L2,L3),
    blocos(L4,L5,L6),
    blocos(L7,L8,L9),

    maplist(label, Linhas).

blocos([], [], []).
blocos([A,B,C|R1], [D,E,F|R2], [G,H,I|R3]) :-
    all_distinct([A,B,C,D,E,F,G,H,I]),
    blocos(R1,R2,R3).
