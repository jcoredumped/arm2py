/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     DIRHEXA = 258,
     ETIQUETA = 259,
     ENTERO = 260,
     ENTERONEGATIVO = 261,
     REGISTRO = 262,
     GLOBAL = 263,
     DATA = 264,
     WORD = 265,
     EQU = 266,
     BSS = 267,
     SPACE = 268,
     TEXT = 269,
     END = 270,
     AND = 271,
     ORR = 272,
     EOR = 273,
     ADD = 274,
     SUB = 275,
     RSB = 276,
     MOV = 277,
     CMP = 278,
     MUL = 279,
     MLA = 280,
     LDR = 281,
     STR = 282,
     B = 283,
     BEQ = 284,
     BNE = 285,
     BHI = 286,
     BLS = 287,
     BGE = 288,
     BLT = 289,
     BGT = 290,
     BLE = 291,
     DP = 292,
     PUNTO = 293,
     IGUAL = 294,
     CA = 295,
     CC = 296,
     COMA = 297,
     ALMOADILLA = 298,
     FL = 299
   };
#endif
/* Tokens.  */
#define DIRHEXA 258
#define ETIQUETA 259
#define ENTERO 260
#define ENTERONEGATIVO 261
#define REGISTRO 262
#define GLOBAL 263
#define DATA 264
#define WORD 265
#define EQU 266
#define BSS 267
#define SPACE 268
#define TEXT 269
#define END 270
#define AND 271
#define ORR 272
#define EOR 273
#define ADD 274
#define SUB 275
#define RSB 276
#define MOV 277
#define CMP 278
#define MUL 279
#define MLA 280
#define LDR 281
#define STR 282
#define B 283
#define BEQ 284
#define BNE 285
#define BHI 286
#define BLS 287
#define BGE 288
#define BLT 289
#define BGT 290
#define BLE 291
#define DP 292
#define PUNTO 293
#define IGUAL 294
#define CA 295
#define CC 296
#define COMA 297
#define ALMOADILLA 298
#define FL 299




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 5 "gramatica.y"
{
    int tipoi;
    char *string;
}
/* Line 1529 of yacc.c.  */
#line 142 "y.tab.h"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

