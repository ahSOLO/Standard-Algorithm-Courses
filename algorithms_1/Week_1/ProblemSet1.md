![q1.png](q1.png)
Answer: n log(n)
If the merge step can still be implemented in O(n) time, then the sorting step will only become less complex as the number of levels of recursion will be done in log3(n) instead of log2(n). The final running time will therefore remain n log(n).

![q2.png](q2.png)
True. log(f(n)^c) will still have a big O of log(n), regardless of how large the constant c is.

![q3.png](q3.png)

Answer: Sometimes yes, sometimes no (depending on f and g) & Yes if f(n) ≤ g(n) for all sufficiently large n. Since big-O notation is interested in preserving the highest growing term in the equation, that specificity must be preserved and therefore this will only be true if g(n) is greater or equal to f(n) for all sufficiently large n.

![q4.png](q4.png)

Answer: Theta of nk^2.

![q5.png](q5.png)

e->a->d->b->c