num_rounds = int(input())
final_score = 0.0
rounds_processed = 0
score = 0.0
for round_num in range(num_rounds):
    score = float(input())
    if score >100: 
        bonus = 20
    else:
        bonus = 0
    final_score += score + (score * bonus / 100)
    rounds_processed += 1

print(f"{final_score:.1f}")
print(rounds_processed)
