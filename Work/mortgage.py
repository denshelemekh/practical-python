# mortgage.py
#
# Exercise 1.7

principal = 500_000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

print(f'MONTH CURR_PAYMENT   TOT_PAID PRINCIPAL')
while True:
    month += 1
    curr_payment = payment

    if month in range(extra_payment_start_month, extra_payment_end_month + 1):
        curr_payment = payment + extra_payment

    principal = principal * (1 + rate / 12) - curr_payment

    if principal < 0:
        delta = 0 - principal
        principal += delta
        curr_payment -= delta

    total_paid = total_paid + curr_payment

    # print(f'MONTH CURR_PAYMENT TOT_PAID PRINCIPAL')
    print(f'{month:>5d} {round(curr_payment, 2):>12.2f} '
          f'{round(total_paid, 2):>10.2f} {round(principal, 2):>9.2f}')

    if principal == 0:
        break

print(f'MONTH CURR_PAYMENT   TOT_PAID PRINCIPAL')
print('\nTotal paid', round(total_paid, 2))
print('Total months', month)
