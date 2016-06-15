def main():
  n = int(input("Enter a number: "))
  result = solve(algorithmImproved, n)
  print 'There are {} occurrences of 2 in the positive integers up to {}'.format(result, n)


  # For double checking
  # for x in range(0, 10000):
  #   bruteForceAnswer = solve(bruteForce, x)
  #   algorithmAnswer = solve(algorithm, x)
  #   algorithmImprovedAnswer = solve(algorithmImproved, x)
  #   if bruteForceAnswer != algorithmAnswer or bruteForceAnswer != algorithmImprovedAnswer:
  #     print "Does not match"
  #     print "Brute Force: " + str(bruteForceAnswer)
  #     print "Algorithm: " + str(algorithmAnswer)
  #     print "Improved Algorithm: " + str(algorithmImprovedAnswer)
  #     return
  
  # print "Congratulations, all the results match"

def solve(alg, n):
  return alg(n)

# Brute Force: Iterate to n, appending each number to a string and then counting all 2s in the string
def bruteForce(n):
  stringArr = []
  for x in range(1, n+1):
    stringArr.append(str(x))

  return ''.join(stringArr).count('2')

# Count all occurences of 2 from right to left, start counting only the twos in the ones place, then tens, then hundreds, etc.
def algorithm(n):
  count = 0
  # When i is 1, looking at ones place, when i is 10, looking at tens place, etc. etc.
  i = 1
  while i <= n:
    # Very first occurence of 2 in the place of the current iteration (2, 20, 200, etc.)
    start = 2 * i
    current = start

    while current <= n:
      # occurs 1 at a time in ones place, 10 at a time in tens palce, 100 at a time in hundreds place, etc. etc.
      if current + i - 1 <= n:
        # n is larger than all occurences we're currently looking at, 20-29, 200-299, etc.
        count += i
      else:
        # n is somewhere in the middle of the occurences, 24 when we're looking at 20-29, etc.
        count += n - current + 1

      # move onto next occurence of 2 in the same place
      current += i * 10

    # Move left and check the next place
    i *= 10

  return count


# Same idea as the first algorithm, but using some math to improve efficiency by removing the inner loop
def algorithmImproved(n):
  count = 0
  i = 1
  while i <= n:
    # Very first occurence of 2 in the place of the current iteration
    start = 2 * i
    # Use division to figure out how many times inner loop would run instead of actually running the inner loop (will not include final loop)
    numLoops = n / (i * 10)
    count += numLoops * i

    # Go straight to the final loop
    final = start + (numLoops * i * 10)

    # Need this check in case there were no loops (eg. checking 10s digit and n is 13)
    if final <= n:
      if final + i - 1 <= n:
        # n is larger than all occurences we're currently looking at, 20-29, 200-299, etc.
        count += i
      else:
        # n is somewhere in the middle of the occurences, 24 when we're looking at 20-29, etc.
        count += n - final + 1

    # Move left and check the next place
    i *= 10

  return count


if __name__ == "__main__":
    main()
