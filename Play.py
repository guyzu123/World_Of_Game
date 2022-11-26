from GuessGame import generate_number,get_gues_from_user,compare_results



secret_number = generate_number()
user_number = get_gues_from_user()
compare_results=compare_results(secret_number,user_number)

print(compare_results)

