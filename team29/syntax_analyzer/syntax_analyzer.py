# File name: syntax_analyzer.py
# Student Number: 20200123
# Student Name: HwangSeoJin

SLR_grammar_dic = {"CODE'": ['CODE'], 'CODE': ['VDECL CODE', 'FDECL CODE', 'FDECL', 'VDECL'], 'VDECL': ['vtype identifier semi'], 'FDECL': ['vtype identifier lparen ARG'], 'ARG': ['vtype identifier MOREARGS', 'rparen lbrace BLOCK'], 'MOREARGS': ['comma vtype identifier MOREARGS', 'rparen lbrace BLOCK'], 'BLOCK': ['STMT BLOCK', 'RETURN rbrace', 'rbrace', 'rbrace else lbrace BLOCK'], 'STMT': ['VDECL', 'identifier assign RHS semi', 'if lparen COND rparen lbrace BLOCK', 'while lparen COND rparen lbrace BLOCK'], 'RHS': ['EXPR', 'literal'], 'EXPR': ['TERM add_sub EXPR', 'TERM'], 'TERM': ['FACTOR mult_div TERM', 'FACTOR'], 'FACTOR': ['lparen EXPR rparen', 'identifier', 'integer'], 'COND': ['FACTOR comparison FACTOR'], 'RETURN': ['return FACTOR semi']}
SLR_grammar = {1: 'CODE -> VDECL CODE', 2: 'CODE -> FDECL CODE', 3: 'CODE -> FDECL', 4: 'CODE -> VDECL', 5: 'VDECL -> vtype identifier semi', 6: 'FDECL -> vtype identifier lparen ARG', 7: 'ARG -> vtype identifier MOREARGS', 8: 'ARG -> rparen lbrace BLOCK', 9: 'MOREARGS -> comma vtype identifier MOREARGS', 10: 'MOREARGS -> rparen lbrace BLOCK', 11: 'BLOCK -> STMT BLOCK', 12: 'BLOCK -> RETURN rbrace', 13: 'BLOCK -> rbrace', 14: 'BLOCK -> rbrace else lbrace BLOCK', 15: 'STMT -> VDECL', 16: 'STMT -> identifier assign RHS semi', 17: 'STMT -> if lparen COND rparen lbrace BLOCK', 18: 'STMT -> while lparen COND rparen lbrace BLOCK', 19: 'RHS -> EXPR', 20: 'RHS -> literal', 21: 'EXPR -> TERM add_sub EXPR', 22: 'EXPR -> TERM', 23: 'TERM -> FACTOR mult_div TERM', 24: 'TERM -> FACTOR', 25: 'FACTOR -> lparen EXPR rparen', 26: 'FACTOR -> identifier', 27: 'FACTOR -> integer', 28: 'COND -> FACTOR comparison FACTOR', 29: 'RETURN -> return FACTOR semi'}

terminals = ['identifier', 'lparen', 'comma', 'add_sub', 'return', 'while', 'rparen', 'rbrace', 'mult_div', 'integer', 'lbrace', 'assign', 'if', 'semi', 'vtype', 'literal', 'comparison', 'else']
nonterminals = ['CODE', 'FDECL', 'STMT', 'RHS', 'FACTOR', 'VDECL', 'ARG', 'RETURN', 'COND', 'EXPR', 'TERM', 'MOREARGS', 'BLOCK']

start_symbol = "CODE'"

parsing_table = {0:{'vtype': 's4', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': 1, 'VDECL': 2, 'FDECL': 3, 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                1: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': 'acc', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                2: {'vtype': 's4', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': 'r4', 'CODE': 5, 'VDECL': 2, 'FDECL': 3, 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                3: {'vtype': 's4', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': 'r3', 'CODE': 6, 'VDECL': 2, 'FDECL': 3, 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                4: {'vtype': '', 'identifier': 's7', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                5: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': 'r1', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                6: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': 'r2', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                7: {'vtype': '', 'identifier': '', 'semi': 's8', 'lparen': 's9', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                8: {'vtype': 'r5', 'identifier': 'r5', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 'r5', 'else': '', 'assign': '', 'if': 'r5', 'while': 'r5', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 'r5', '$': 'r5', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                9: {'vtype': 's11', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': 's12', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': 10, 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                10: {'vtype': 'r6', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': 'r6', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                11: {'vtype': '', 'identifier': 's13', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                12: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': 's14', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                13: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': 's17', 'lbrace': '', 'comma': 's16', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': 15, 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                14: {'vtype': 's27', 'identifier': 's23', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 's21', 'else': '', 'assign': '', 'if': 's24', 'while': 's25', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 's26', '$': '', 'CODE': '', 'VDECL': 22, 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': 18, 'STMT': 19, 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': 20}, 
                15: {'vtype': 'r7', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': 'r7', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                16: {'vtype': 's28', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                17: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': 's29', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                18: {'vtype': 'r8', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': 'r8', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                19: {'vtype': 's27', 'identifier': 's23', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 's21', 'else': '', 'assign': '', 'if': 's24', 'while': 's25', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 's26', '$': '', 'CODE': '', 'VDECL': 22, 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': 30, 'STMT': 19, 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': 20}, 
                20: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 's31', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                21: {'vtype': 'r13', 'identifier': 'r13', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 'r13', 'else': 's32', 'assign': '', 'if': 'r13', 'while': 'r13', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 'r13', '$': 'r13', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                22: {'vtype': 'r15', 'identifier': 'r15', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 'r15', 'else': '', 'assign': '', 'if': 'r15', 'while': 'r15', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 'r15', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                23: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': 's33', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                24: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': 's34', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                25: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': 's35', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                26: {'vtype': '', 'identifier': 's38', 'semi': '', 'lparen': 's37', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': 's39', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': 36, 'COND': '', 'RETURN': ''}, 
                27: {'vtype': '', 'identifier': 's40', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                28: {'vtype': '', 'identifier': 's41', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                29: {'vtype': 's27', 'identifier': 's23', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 's21', 'else': '', 'assign': '', 'if': 's24', 'while': 'r25', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 's26', '$': '', 'CODE': '', 'VDECL': 22, 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': 42, 'STMT': 19, 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': 20}, 
                30: {'vtype': 'r11', 'identifier': 'r11', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 'r11', 'else': '', 'assign': '', 'if': 'r11', 'while': 'r11', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 'r11', '$': 'r11', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                31: {'vtype': 'r12', 'identifier': 'r12', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 'r12', 'else': '', 'assign': '', 'if': 'r12', 'while': 'r12', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 'r12', '$': 'r12', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                32: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': 's43', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                33: {'vtype': '', 'identifier': 's38', 'semi': '', 'lparen': 's37', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': 's46', 'add_sub': '', 'mult_div': '', 'integer': 's39', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': 44, 'EXPR': 45, 'TERM': 47, 'FACTOR': 48, 'COND': '', 'RETURN': ''}, 
                34: {'vtype': '', 'identifier': 's38', 'semi': '', 'lparen': 's37', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': 's39', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': 50, 'COND': 49, 'RETURN': ''}, 
                35: {'vtype': '', 'identifier': 's38', 'semi': '', 'lparen': 's37', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': 's39', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': 50, 'COND': 51, 'RETURN': ''}, 
                36: {'vtype': '', 'identifier': '', 'semi': 's52', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                37: {'vtype': '', 'identifier': 's38', 'semi': '', 'lparen': 's37', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': 's39', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': 53, 'TERM': 47, 'FACTOR': 48, 'COND': '', 'RETURN': ''},
                38: {'vtype': '', 'identifier': '', 'semi': 'r26', 'lparen': '', 'rparen': 'r26', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': 'r26', 'mult_div': 'r26', 'integer': '', 'comparison': 'r26', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                39: {'vtype': '', 'identifier': '', 'semi': 'r27', 'lparen': '', 'rparen': 'r27', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': 'r27', 'mult_div': 'r27', 'integer': '', 'comparison': 'r27', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                40: {'vtype': '', 'identifier': '', 'semi': 's8', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                41: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': 's17', 'lbrace': '', 'comma': 's16', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': 54, 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                42: {'vtype': 'r10', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': 'r10', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                43: {'vtype': 's27', 'identifier': 's23', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 's21', 'else': '', 'assign': '', 'if': 's24', 'while': 's25', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 's26', '$': '', 'CODE': '', 'VDECL': 22, 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': 55, 'STMT': 19, 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': 20}, 
                44: {'vtype': '', 'identifier': '', 'semi': 's56', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                45: {'vtype': '', 'identifier': '', 'semi': 'r19', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                46: {'vtype': '', 'identifier': '', 'semi': 'r20', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                47: {'vtype': '', 'identifier': '', 'semi': 'r22', 'lparen': '', 'rparen': 'r22', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': 's57', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                48: {'vtype': '', 'identifier': '', 'semi': 'r24', 'lparen': '', 'rparen': 'r24', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': 'r24', 'mult_div': 's58', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                49: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': 's59', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                50: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': 's60', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                51: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': 's61', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                52: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 'r29', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                53: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': 's62', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                54: {'vtype': 'r9', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': 'r9', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                55: {'vtype': 'r14', 'identifier': 'r14', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 'r14', 'else': '', 'assign': '', 'if': 'r14', 'while': 'r14', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 'r14', '$': 'r14', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                56: {'vtype': 'r16', 'identifier': 'r16', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 'r16', 'else': '', 'assign': '', 'if': 'r16', 'while': 'r16', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 'r16', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                57: {'vtype': '', 'identifier': 's38', 'semi': '', 'lparen': 's37', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': 's39', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': 63, 'TERM': 47, 'FACTOR': 48, 'COND': '', 'RETURN': ''}, 
                58: {'vtype': '', 'identifier': 's38', 'semi': '', 'lparen': 's37', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': 's39', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': 64, 'FACTOR': 48, 'COND': '', 'RETURN': ''}, 
                59: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': 's65', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                60: {'vtype': '', 'identifier': 's38', 'semi': '', 'lparen': 's37', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': 's39', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': 66, 'COND': '', 'RETURN': ''}, 
                61: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': 's67', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                62: {'vtype': '', 'identifier': '', 'semi': 'r25', 'lparen': '', 'rparen': 'r25', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': 'r25', 'mult_div': 'r25', 'integer': '', 'comparison': 'r25', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                63: {'vtype': '', 'identifier': '', 'semi': 'r21', 'lparen': '', 'rparen': 'r21', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                64: {'vtype': '', 'identifier': '', 'semi': 'r23', 'lparen': '', 'rparen': 'r23', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': 'r23', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                65: {'vtype': 's27', 'identifier': 's23', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 's21', 'else': '', 'assign': '', 'if': 's24', 'while': 's25', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 's26', '$': '', 'CODE': '', 'VDECL': 22, 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': 68, 'STMT': 19, 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': 20}, 
                66: {'vtype': '', 'identifier': '', 'semi': '', 'lparen': '', 'rparen': 'r28', 'lbrace': '', 'comma': '', 'rbrace': '', 'else': '', 'assign': '', 'if': '', 'while': '', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': '', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                67: {'vtype': 's27', 'identifier': 's23', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 's21', 'else': '', 'assign': '', 'if': 's24', 'while': 's25', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 's26', '$': '', 'CODE': '', 'VDECL': 22, 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': 69, 'STMT': 19, 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': 20}, 
                68: {'vtype': 'r17', 'identifier': 'r17', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 'r17', 'else': '', 'assign': '', 'if': 'r17', 'while': 'r17', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 'r17', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}, 
                69: {'vtype': 'r18', 'identifier': 'r18', 'semi': '', 'lparen': '', 'rparen': '', 'lbrace': '', 'comma': '', 'rbrace': 'r18', 'else': '', 'assign': '', 'if': 'r18', 'while': 'r18', 'literal': '', 'add_sub': '', 'mult_div': '', 'integer': '', 'comparison': '', 'return': 'r18', '$': '', 'CODE': '', 'VDECL': '', 'FDECL': '', 'ARG': '', 'MOREARGS': '', 'BLOCK': '', 'STMT': '', 'RHS': '', 'EXPR': '', 'TERM': '', 'FACTOR': '', 'COND': '', 'RETURN': ''}}


# input (using lexical_analyzer output!)
lexical_file = open('lexical_test.out','r')
# input lexemes for pointing out where error has occured
lexeme_file = open('lexical_lexeme.out', 'r')

# ouput (syntax analyzer output : whether the grammar is accepted or not)
syntax_file = open('syntax_test.out','w')

# lexemes for pointing out where error has occured
lexemes = lexeme_file.read()
# file input uses as a string.
lexical_output = lexical_file.read().lower()

token_stream = (lexical_output + " $").split()
lexeme_stream = (lexemes).split()

# for counting steps 
step_num = 0
# stack neeed for parsing
syntax_stack = ['0']

pointer = 0
token = token_stream[pointer]


# Method to find First set.
def FIRST_SET(nonterminal):
    # if it is terminal, just return!
    if nonterminal in terminals:
        return {nonterminal}
    
    first = set([])

    first_list = [nonterminal]

    for next_symbol in SLR_grammar_dic[nonterminal]:
        for (i, next) in enumerate(next_symbol.split()):
            length = len(next_symbol)

            if next not in first_list:
                # check next's FIRST SET
                symbol_first = FIRST_SET(next)

                for temp in symbol_first:
                    if temp in terminals:
                        first.add(temp)

                if '^' not in symbol_first:
                    break
            else:
                break

            if i + 1 == length:
                first.add('^')

    first_list.remove(nonterminal)

    return first

# Method to find FOLLOW set.
def FOLLOW_SET(nonterminal):

    follow = set([])
    follow_list = [nonterminal]

    # starting symbol add $
    if nonterminal == start_symbol:
        follow.add('$')

    for (before, next_symbols) in SLR_grammar_dic.items():
        for next in next_symbols:
            next = next.split()

            if nonterminal in next[:-1]:
                index_search = next.index(nonterminal) + 1
                
                first = FIRST_SET(next[index_search])
                follow = follow | (first - set('^'))

                if '^' in first:
                    if before not in follow_list:
                        follow = follow | FOLLOW_SET(before)

            elif nonterminal in next[-1]:
                if before not in follow_list:
                    follow = follow | FOLLOW_SET(before)

    follow_list.remove(nonterminal)

    return follow


# SLR Parser to check whether the Grammar is accepted or not.
while 1:
    try:
        step_num += 1
        state = int(syntax_stack[-1])

        # If there is no Symbols in parsing table, print ERROR & break
        if token not in parsing_table[state].keys():
            error_message = "\nERROR occured at : " + str(step_num) + "\n"
            print("\nREJECTED! THERE IS NO MATCHING SYMBOL NAMED" + token + "\n")
            print(error_message)
            break

        # If all grammar accepted, write and print accept message & break
        elif parsing_table[state][token] == "acc":
            accept_message = "\nACCEPTED! GRAMMATICALLY CORRECT\n"
            syntax_file.write(accept_message)
            print(accept_message)
            break

        # GOTO
        elif parsing_table[state][token][0] == "r":
            next_state = int(parsing_table[state][token][1:])
            grammar = SLR_grammar[next_state].split()

            if grammar[-1] != '^':
                after_index = grammar.index('->') + 1
                boundary_len = 2 * len(grammar[after_index:])
                
                syntax_stack = syntax_stack[:-(boundary_len)]
                state = int(syntax_stack[-1])
                
                before = grammar[0]
                syntax_stack.append(before)

                next_state_num = str(parsing_table[state][before])
                syntax_stack.append(next_state_num)

        # ACTION
        elif parsing_table[state][token][0] == "s":
            next_state = parsing_table[state][token][1:]
            
            syntax_stack.append(token)
            syntax_stack.append(next_state)
            
            pointer += 1
            token = token_stream[pointer]


    # IndexError(In this program, It means grammatical error)!
    # Error report which explains why and where the Error occured.
    except IndexError:
        error_message = "\nREJECTED! \n" + "\nGRAMMATICAL ERROR found at : " + str(step_num) + "th lexeme(token)'" + lexeme_stream[step_num-1] + "'\n"
        syntax_file.write(error_message)
        print(error_message)
        break

    # TypeError!
    # Error report which explains why and where the Error occured.
    except TypeError:
        error_message = "\nREJECTED! \n" + "\nTYPE ERROR occured at : " + str(step_num) + "\n"
        syntax_file.write(error_message)
        print(error_message)
        break


#file close.
lexical_file.close()
lexeme_file.close()
syntax_file.close()

