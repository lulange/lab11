# Presidio anonymizer

# lab11

- Identify how many if/elif branches the factory uses to select the operator.

There were two if statements used to check for errors in the function inputs. Otherwise there are
no required conditional statements to select the operator. This is because the operators factory uses
dictionaries to map operator names to operator classes for all base operators.

- Identify the exact Python data structure used to select operators.

Python has dictionaries which act like hashmaps. That is the data structure used in this example since
operator name is going to be known at runtime.

- Explain how this demonstrates the Strategy design pattern.

This data structure helps the strategy design pattern function by facilitating the swapping of strategies
by mapping the key (operator name) to the strategy (operator). This means that the operator can be chosen 100% based
on the parameter given for operator name.

