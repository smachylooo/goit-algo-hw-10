import timeit

COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount: int) -> dict[int, int]:
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    result = {}

    for coin in COINS:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count

    return result

def find_min_coins(amount: int) -> dict[int, int]:
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    min_coins = [0] + [float("inf")] * amount
    last_coin = [0] * (amount + 1)
    for current_amount in range(1, amount + 1):
        for coin in COINS:
            if coin <= current_amount and min_coins[current_amount - coin] + 1 < min_coins[current_amount]:
                min_coins[current_amount] = min_coins[current_amount - coin] + 1
                last_coin[current_amount] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result

def compare_algorithms(amount: int, repeat_count: int = 1000) -> None:
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=repeat_count)
    dp_time = timeit.timeit(lambda: find_min_coins(amount), number=repeat_count)
    print(f"Amount: {amount}")
    print(f"Greedy result: {find_coins_greedy(amount)}")
    print(f"Dynamic programming result: {find_min_coins(amount)}")
    print(f"Greedy time for {repeat_count} runs: {greedy_time:.6f} seconds")
    print(f"Dynamic programming time for {repeat_count} runs: {dp_time:.6f} seconds")

if __name__ == "__main__":
    test_amounts = [113, 999, 10_000]
    for amount in test_amounts:
        compare_algorithms(amount)
        print("-" * 60)
