import math
import argparse

parser = argparse.ArgumentParser(description="This program is used to calculate differential or annuity payments.")
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()

if args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters")
    exit()

if args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    exit()

if args.interest is None:
    print("Incorrect parameters")
    exit()

i = (float(args.interest) / 100) / 12
if args.type == "annuity":
    if args.principal is None:
        periods = int(args.periods)
        P = (int(args.payment) / ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1)))
        print(P)
    elif args.payment is None:
        prin = int(args.principal)
        periods = int(args.periods)
        annuity = prin * ((i * ((1 + i) ** periods)) / (((1 + i) ** periods) - 1))
        print(annuity)
    elif args.periods is None:
        payment = int(args.payment)
        prin = int(args.principal)
        temp = (payment / (payment - i * prin))
        n = math.ceil(math.log(temp, 1 + i))
        if n > 12:
            years = int(n / 12)
            overpayment = (payment * n) - prin
            print(f"It will take {years} years and overpayment is {overpayment}!")
        else:
            print(f"It will take {n} months to repay this loan!")
else:
    full = 0
    principal = int(args.principal)
    periods = int(args.periods)
    for j in range(1, periods + 1):
        dm = math.ceil(principal / periods + (i * (principal - ((principal * (j - 1)) / periods))))
        full += dm
        print(f"month {j}: payment is {dm}")
    overpayment = math.ceil(full - principal)
    print(f"Overpayment = {overpayment}")
