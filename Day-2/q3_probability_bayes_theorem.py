total_emails = int(input("Enter total number of emails: "))
emails_with_free = int(input("Enter number of emails containing 'free': "))
spam_emails = int(input("Enter number of spam emails: "))
spam_and_free = int(input("Enter number of emails that are both spam and contain 'free': "))

# Calculate probabilities using Bayes' Theorem
p_spam = spam_emails / total_emails
p_free = emails_with_free / total_emails   
p_free_given_spam = spam_and_free / spam_emails
p_spam_given_free = (p_free_given_spam * p_spam) / p_free
    
print(f"P(Spam | Free): {p_spam_given_free:.4f}")