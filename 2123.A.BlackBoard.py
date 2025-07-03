# A. Blackboard Game
# time limit per test1 second
# memory limit per test256 megabytes
# Initially, the integers from 0
#  to 𝑛−1
#  are written on a blackboard.

# In one round,

# Alice chooses an integer 𝑎
#  on the blackboard and erases it;
# then Bob chooses an integer 𝑏
#  on the blackboard such that 𝑎+𝑏≡3(mod4)
# ∗
#  and erases it.
# Rounds take place in succession until a player is unable to make a move — the first player who is unable to make a move loses. Determine who wins with optimal play.

# ∗
# We define that 𝑥≡𝑦(mod𝑚)
#  whenever 𝑥−𝑦
#  is an integer multiple of 𝑚
# .

# Input
# The first line contains an integer 𝑡
#  (1≤𝑡≤100
# )  — the number of test cases.

# The only line of each test case contains an integer 𝑛
#  (1≤𝑛≤100
# ) — the number of integers written on the blackboard.

# Output
# For each test case, output on a single line "Alice" if Alice wins with optimal play, and "Bob" if Bob wins with optimal play.

# You can output the answer in any case (upper or lower). For example, the strings "aLiCe", "alice", "ALICE", and "alICE" will be recognized as "Alice".

# Example
# InputCopy
# 5
# 2
# 4
# 5
# 7
# 100
# OutputCopy
# Alice
# Bob
# Alice
# Alice
# Bob

t = int(input())

for _ in range(t):
    n = int(input())
    if n % 4 == 0:
        print("Bob")
    else:
        print("Alice")