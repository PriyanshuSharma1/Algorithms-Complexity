def lcs_top_down(A, B):
    m = len(A) + 1
    n = len(B) + 1


    # Initialize a 2D list with 'm' rows and 'n' columns, all elements set to 0
    dp = [[0 for column in range(n)] for row in range(m)]

    # Fill the dp array using the top-down approach
    for i in range(1, m):
        for j in range(1, n):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                print("Match found at A[{}] = {} and B[{}] = {}".format(i-1, A[i-1], j-1, B[j-1]))
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            for row in dp:
                print(' '.join(map(str, row)))
            print("\n")    
    return dp

def print_matrix(dp):
    for row in dp:
        print(' '.join(map(str, row)))

def main():
    A = "AC"
    B = "TAGC"
    
    dp = lcs_top_down(A, B)
    
    print("DP Matrix:")
    print_matrix(dp)

if __name__ == "__main__":
    main()