def main():

    org_str = 'Python Programming'
    ##################################################
    # Comlete your code here
    ##################################################
    sub1 = org_str[:6]
    sub2 = org_str[7:]
    merge_str = sub2 + ' ' + sub1
    print(sub2)
    print(sub1)
    print(merge_str)

    #########################################
    # Do not delete the return statement
    return sub1, sub2, merge_str


if __name__ == '__main__':
    main()
