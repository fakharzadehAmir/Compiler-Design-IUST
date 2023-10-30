grammar Arithmetic;

start: expr EOF;
expr returns[value=float()]: term ((ADD | SUB) term)*;
term returns[value=float()]: factor ((MUL | DIV) factor)*;
factor returns[value=float()]: NUMBER | LPAREN expr RPAREN;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
NUMBER: [0-9]+ | [0-9]*'.'[0-9]*;
WS: [ \t\r\n]+ -> skip;