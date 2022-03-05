
"""
    A program to generate N number of coupons until all of them are unique
                                                                            """

import random


def checkCoupon():  # function to look for coupons until all of them are unique
    collect = []

    while True:
        coupon = int(random.random() * 100)  # generate coupon number

        if coupon in collect:  # condition for similar coupon
            print("\nSimilar coupon found\n")
            break
        else:
            collect.append(coupon)  # add unique

    print("Unique coupons are: ", collect)
    print()
    print("Total no. of random coupons: ", len(collect))  # output


if __name__ == '__main__':
    print("\nGenerating coupons for you...")
    checkCoupon()  # function calling
