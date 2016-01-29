"""sanity.py

Let's try a simpler language first.

Pattern
  VariablePattern
    name - String
  TemplatePattern
    name - String
    type_arguments - [Pattern]

Type:
  name - String
  type_arguments - [Type]

Typedef:
  name - String
  type_arguments - [Pattern]
  type - Type

Class:
  name - String
  type_arguments - [Pattern]
  returns - Type
  fields - [(String, Type)]

Function:
  name - String
  arguments - [(String, Statement)]
  body - [Statement]

Statement
  Block:
    statements - [Statement]
  Return:
    value - Expression
  While:
    condition - Expression
    body - Statement
  If:
    condition - Expression
    body - Statement
    other - Statement?
  Expression
    FunctionCall:
      name - String
      type_arguments - [Type]
    Name:
      name - String

=======

For runtime polymorphism, consider:

# 'Union' should probably be implemented natively.
class Union[Left, Right] {
  Bool which # false -> Left, true -> Right
  Left left
  Right right
}

typedef ...

Or maybe, I could implement some sort of function pointer...

I think there could be a safe way to do this.

=======

"""
