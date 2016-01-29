"""sanity.py

Statement
  Return:
    value - [Expression]
  While
  If
  Block:
    statements - [Statement]
  Expression
    FunctionCall:
      name - String
      typeargs - [Type]?
      args - [Expression]
    Name:
      name - String
    String:
      value - String
    Int:
      value - String
    Float:
      value - String
    List:
      values - [Expression]
    Or:
      left - Expression
      right - Expression
    And:
      left - Expression
      right - Expression

Function:
  name - String
  typeargs - [Pattern]?
  args - [(String, Pattern)]
  body - Statement

"""


