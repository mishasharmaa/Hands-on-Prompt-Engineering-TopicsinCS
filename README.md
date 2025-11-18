# Hands-on-Prompt-Engineering-TopicsinCS

## Part 1 - Define Task 

python3 part1_define_task.py 
=== TASK DESCRIPTION === 
Task: Classify short customer messages as POSITIVE, NEGATIVE, or NEUTRAL. Good output gives correct label + short explanation. 
=== QUALITY CRITERIA === 
1. Correct sentiment label. 
2. Short, clear explanation. 
3. Format: <LABEL> - <reason>. 
=== EVAL SET === 
1. The product is amazing! 
2. It stopped working after one day. 
3. It's okay, nothing special. 
4. I love the design but shipping was slow. 
5. Worst purchase ever.

--- 

## Part 2 - Baseline Prompting 

python3 part2_zero_shot.py
=== ZERO SHOT RESULTS === 
Input: The product is amazing! 
Output: POSITIVE - Expresses positive sentiment. 

Input: It stopped working after one day. 
Output: NEGATIVE - Stopped working after one day. 

Input: It's okay, nothing special. 
Output: NEUTRAL - Indicates a lack of strong positive or negative sentiment. 

Input: I love the design but shipping was slow. 
Output: POSITIVE - positive sentiment expressed, despite a negative aspect. 

Input: Worst purchase ever. 
Output: NEGATIVE - Expresses extreme dissatisfaction.

--- 

## Part 3 - Improve with Shots & Structure

python3 part3_improvements.py 
=== FEW SHOT === 
The product is amazing! 
POSITIVE - expresses strong approval and excitement 

It stopped working after one day. 
NEGATIVE - expresses dissatisfaction with the product's short lifespan. 

It's okay, nothing special. 
NEUTRAL - expresses an average or indifferent sentiment. 

I love the design but shipping was slow. 
MIXED - expresses both positive (love the design) and negative (shipping was slow) sentiments. 

Worst purchase ever. 
NEGATIVE - expresses strong dislike and regret. 

=== CHAIN OF THOUGHT === 
The product is amazing! 
The message expresses strong positive feelings about the product. There are no negative or neutral terms. 
Final Answer: POSITIVE - The word "amazing" clearly expresses positive sentiment. 

It stopped working after one day. 
The message indicates a negative experience because the product malfunctioned quickly. 
Final Answer: NEGATIVE - Product stopped working after a short time. 

It's okay, nothing special. 
Okay, let's analyze the sentiment of the message "It's okay, nothing special." 
* **"It's okay"**: This indicates a neutral or slightly positive sentiment. It suggests that something is acceptable or passable. 
* **"nothing special"**: This phrase indicates a negative sentiment because it means that something is not particularly good or noteworthy. 
* **Combined**: When combined, the phrase presents a somewhat neutral sentiment. It is neither bad nor good; it's just average. 
<NEUTRAL> - The phrase contains both slightly positive ("okay") and negative ("nothing special") elements, resulting in a neutral overall sentiment. 

I love the design but shipping was slow. 
The message expresses both positive and negative sentiments. "I love the design" clearly indicates a positive feeling. "Shipping was slow" expresses a negative experience. Overall it is mixed sentiment. 
MIXED - Contains both positive and negative sentiments. 

Worst purchase ever. The message is short and direct, expressing strong dissatisfaction. "Worst" is a superlative indicating the lowest possible quality, and "ever" emphasizes the feeling. 
Final Answer: NEGATIVE - The message uses the superlative "worst" to express extreme dissatisfaction. 

=== SELF CRITIQUE === 
The product is amazing! 
Here's my analysis: 
1. **Analyze the message:** The message expresses a strong positive opinion about the product using the word "amazing." 
2. **Determine the sentiment:** The word "amazing" clearly indicates a positive sentiment. 
3. **Output label and reason:** 
POSITIVE - The message uses the word "amazing," which is a strong indicator of positive sentiment. 

It stopped working after one day. 
1. The message indicates a negative experience with a product or service. 
2. The phrase "stopped working" is a clear indicator of a problem. 
3. "After one day" suggests the problem occurred very soon after the product was received, further intensifying the negative sentiment. 
4. <LABEL> - Negative sentiment because something broke quickly 
5. <LABEL> - NEGATIVE - The product failing after only one day of use indicates dissatisfaction and a negative experience. 

It's okay, nothing special. 
1. The message contains both a positive sentiment ("okay") and a neutral sentiment ("nothing special"). 
2. The phrase "nothing special" tends to slightly outweigh the positive "okay" pulling the overall sentiment towards neutral. 
3. <NEUTRAL> - The message expresses a mild positive sentiment that is offset by a neutral statement. 

I love the design but shipping was slow. 
1. The message contains both positive and negative sentiments. 
2. "I love the design" indicates a positive sentiment. "shipping was slow" indicates a negative sentiment. 
3. Overall, it is mixed. 
MIXED - The message contains both positive sentiment ("I love the design") and negative sentiment ("shipping was slow"). 

Worst purchase ever. 
1. The message expresses strong dissatisfaction. 
2. The word "worst" indicates a negative sentiment. 
OUTPUT: NEGATIVE - The word "worst" expresses a negative sentiment.

---

## Part 4 - Prompt Attacks
part4_prompt_attacks.py 
=== ATTACK RESULT === 
NEGATIVE

---

## Part 5 - Mini Report 

1. Task Description & Eval Set

The task is sentiment classification of short customer messages. The model must label each input as POSITIVE, NEGATIVE, NEUTRAL, or MIXED, and support each label with a short justification.