# File name: lexical_analyzer.py
# Student Number: 20200123
# Team: team 29
# Student Name: Hwang seo-jin


# define TOKENS 
keyword = ['IF', 'if', 'ELSE' , 'else', 'WHILE', 'while', 'return', 'RETURN']
type_int = ['int', 'INT']
type_char = ['char', 'CHAR']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
operator = ['=', '<', '>', '<=', '>=', '==', '!=']
add_sub = ['+', '-']
mult_div = ['*', '/']
terminate_symbol = [';']
white_space = [ '\n' , '\t', ' ']
pair_symbol = ['{', '}', '(', ')']
comma = [',']

# Merge all of Tokens
MERGED = number + letter + add_sub + mult_div + terminate_symbol + pair_symbol + keyword + type_int + comma + type_char + operator + white_space

# return Boolean based on following dfa which is accepted or not.
def accepted_by_dfa(transitions, initial, accepting, string):
    state = initial
    for char in string:
        if char in transitions[state].keys():
             state = transitions[state][char]
        else:
            return bool(0)
    whether_accepted = state in accepting
    return whether_accepted

# Integer DFA
Integer_dfa = {0:{'0':3,'-':1, '1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2,'8':2,'9':2},
               1:{'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2, '8':2,'9':2},
               2:{'0':2,'1':2,'2':2,'3':2,'4':2,'5':2,'6':2,'7':2, '8':2,'9':2},
               3:{}}

# Literal DFA
Literal_dfa = { 0:{'"':1},
              1:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,
                 'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1,
                 '0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'A':1,'B':1,'C':1,
                 'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,'K':1,'L':1,'M':1,'N':1,'O':1,'P':1,'Q':1,
                 'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,'Y':1,'Z':1,'\n':1,'\t':1,' ':1,'"':2},
              2:{}}

# Identifier DFA
Identifier_dfa = { 0:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,
                    'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1},
                 1:{'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,'g':1,'h':1,'i':1,'j':1,'k':1,'l':1,'m':1,
                    'n':1,'o':1,'p':1,'q':1,'r':1,'s':1,'t':1,'u':1,'v':1,'w':1,'x':1,'y':1,'z':1,
                    '0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'A':1,'B':1,'C':1,
                    'D':1,'E':1,'F':1,'G':1,'H':1,'I':1,'J':1,'K':1,'M':1,'N':1,'0':1,'P':1,'Q':1,
                    'R':1,'S':1,'T':1,'U':1,'V':1,'W':1,'X':1,'Y':1,'Z':1}}

# open the file
file = open('test.c','r')
str = file.read()

# save it on the test.out
fileout = open('lexical_test.out','w')
fileout_lexeme = open('lexical_lexeme.out', 'w')
print("    <Lexical Analyzer Table>    ")
print("________________________________")

lexeme=''
blank=' '

# i is index of 'str' and char is value of 'str' about index.
for i,char in enumerate(str):
    # Exclude whit_space in lexical table.
    if char not in white_space:
        lexeme += char

    if (i+1) < len(str):
        # to prevent errors in comparison_operators
        if (str[i] in operator) and str[i + 1] == '=':
            continue
        
        # MERGED is all of tokens.
        elif str[i+1] == blank or str[i+1] in MERGED or lexeme in MERGED :
            # started with '"' -> so it has to end with '"' -> most priority
            if lexeme != '' and lexeme[0] == '"':
                if lexeme[-1] != '"' or len(lexeme) == 1:
                    continue

            # Devide Tokens more specific.
            if lexeme in type_int:
                if str[i+1] not in number+letter:
                    token_name = 'VTYPE'
                else:
                    continue
            
            elif lexeme in type_char:
                if str[i+1] not in number+letter:
                    token_name = 'VTYPE'
                else:
                    continue
            
            elif lexeme == 'return':
                token_name = 'RETURN'
            
            elif lexeme == '(':
                token_name = 'LPAREN'
            
            elif lexeme == ')':
                token_name = 'RPAREN'
            
            elif lexeme == '{':
                token_name = 'LBRACE'
            
            elif lexeme == '}':
                token_name = 'RBRACE'
            
            elif lexeme == '=':
                token_name = 'ASSIGN'
            
            elif lexeme == 'while' and str[i+1] not in number+letter:
                token_name ='WHILE'
            
            elif lexeme == 'else' and str[i+1] not in number+letter:
                token_name ='ELSE'
            
            elif lexeme == 'if' and str[i+1] not in number+letter:
                token_name = 'IF'
            
            # Use Integer DFA
            elif accepted_by_dfa(Integer_dfa,0,{2}|{3},lexeme):
                if str[i+1] not in number:
                    token_name = 'INTEGER'
                else:
                    continue

            # Use Literal DFA
            elif accepted_by_dfa(Literal_dfa,0,{2},lexeme):
                token_name = 'LITERAL'
            
            # Use Identifier DFA
            elif accepted_by_dfa(Identifier_dfa, 0, {1}, lexeme):
                if accepted_by_dfa(Identifier_dfa, 0, {1}, lexeme+str[i+1]) == False:
                    token_name = 'IDENTIFIER'
                else:
                    continue
            
            elif lexeme in add_sub:
                # additional code to tell apart operator '-' and the part of signed integer '-'
                # If there are any operator just before '-', it becomes integer except blank
                if str[i] == '-':
                    d = i-1
                    
                    while str[d] == blank:
                        d -= 1
                    
                    if str[d] in operator or str[d] in add_sub:
                        continue
                
                token_name = 'ADD_SUB'
            
            elif lexeme in mult_div:
                token_name = 'MULT_DIV'
            
            elif lexeme in operator:
                token_name = 'COMPARISON'
            
            elif lexeme == ',':
                token_name = 'COMMA'
            
            elif lexeme == ';':
                token_name = 'SEMI'
            
            if lexeme != '':
                temp = lexeme.replace('\n','<next line>')
                # print too! to check whether we are on the right track
                print('%-15s|  %-15s' % (token_name, lexeme))
                fileout.write(token_name + ' ')
                fileout_lexeme.write(lexeme + ' ') 
                lexeme = ''


    #This is because of the end of 'str'. So it is same as upside.
    elif  i+1 == len(str) :
        if lexeme in 'int':
            last_char_token_name = 'VTYPE'
        
        elif lexeme == 'char':
            last_char_token_name = 'VTYPE'
        
        elif lexeme == '(':
            last_char_token_name = 'LPAREN'
        
        elif lexeme == ')':
            last_char_token_name = 'RPAREN'
        
        elif lexeme == '{':
            last_char_token_name = 'LBRACE'
        
        elif lexeme == '}':
            last_char_token_name = 'RBRACE'
        
        elif accepted_by_dfa(Integer_dfa, 0, {2} | {3}, lexeme):
            last_char_token_name = 'INTEGER'
        
        elif accepted_by_dfa(Literal_dfa, 0, {2}, lexeme):
            last_char_token_name = 'LITERAL'
        
        elif accepted_by_dfa(Identifier_dfa, 0, {1}, lexeme):
            last_char_token_name = 'IDENTIFIER'
        
        elif lexeme in white_space:
            last_char_token_name = 'WHITESPACE'
        
        elif lexeme in add_sub:
            last_char_token_name = 'ADD_SUB'
        
        elif lexeme in mult_div:
            last_char_token_name = 'MULT_DIV'
       
        elif lexeme in keyword:
            last_char_token_name = 'KEYWORD'
        
        elif lexeme in operator:
            last_char_token_name = 'COMPARISON'
        
        elif lexeme == 'return':
            last_char_token_name = 'RETURN'
        
        elif lexeme == ',':
            last_char_token_name = 'COMMA'
        
        elif lexeme == ';':
            last_char_token_name = 'SEMI'
        
        elif lexeme == '=':
            last_char_token_name = 'ASSIGNMENT'
        
        if lexeme != '':
            # print too! to check whether we are on the right track
            print('%-15s|  %-15s' % (last_char_token_name, lexeme))
            fileout.write(last_char_token_name)
            fileout_lexeme.write(lexeme)
            lexeme = ''
            


file.close()
fileout.close()