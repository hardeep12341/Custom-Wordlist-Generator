#!/usr/bin/env python3

import itertools

print("=" * 50)
print("          CUSTOM WORDLIST MAKER")
print("          CTF / AUTHORIZED LAB")
print("=" * 50)

# ------------------------------------------
# Get information
# ------------------------------------------

fields = [
    "Name / Nickname",
    "Favorite Game",
    "Favorite Song / Artist",
    "Pet Name",
    "City",
    "Favorite Team",
    "Important Year"
]

words = []

print("\nEnter information.")
print("Press ENTER to skip any field.\n")

for field in fields:
    value = input(f"{field}: ").strip()

    if value:
        words.append(value)


if not words:
    print("\nNo information entered.")
    exit()


# ------------------------------------------
# Options
# ------------------------------------------

print("\n========== OPTIONS ==========")

use_numbers = input(
    "Use numbers? (y/n): "
).lower() == "y"

use_special = input(
    "Use special characters? (y/n): "
).lower() == "y"

use_two_words = input(
    "Generate 2-word combinations? (y/n): "
).lower() == "y"

use_three_words = input(
    "Generate 3-word combinations? (y/n): "
).lower() == "y"


# ------------------------------------------
# Choose special characters
# ------------------------------------------

specials = []

if use_special:

    print("\nChoose special characters.")

    print("Example: !@#$%_-.")

    special_input = input(
        "Enter characters [!@#$%_- .]: "
    ).strip()

    if not special_input:
        special_input = "!@#$%_-."

    specials = list(special_input)


# ------------------------------------------
# Numbers
# ------------------------------------------

numbers = [
    "0",
    "1",
    "12",
    "123",
    "1234",
    "007",
    "111",
    "222",
    "321",
    "2024",
    "2025",
    "2026"
]


# ------------------------------------------
# Separators
# ------------------------------------------

separators = [
    "",
    "_",
    "-",
    "."
]


# ------------------------------------------
# Create word variations
# ------------------------------------------

variations = set()

for word in words:

    variations.add(word)
    variations.add(word.lower())
    variations.add(word.upper())
    variations.add(word.capitalize())


# ------------------------------------------
# Result set
# ------------------------------------------

result = set()


# ------------------------------------------
# Single words
# ------------------------------------------

print("\nGenerating single-word variations...")

for word in variations:

    result.add(word)

    # Numbers
    if use_numbers:

        for number in numbers:

            result.add(word + number)
            result.add(number + word)

    # Special characters
    if use_special:

        for special in specials:

            result.add(word + special)
            result.add(special + word)

            if use_numbers:

                for number in numbers:

                    result.add(
                        word + special + number
                    )

                    result.add(
                        word + number + special
                    )

                    result.add(
                        special + word + number
                    )


# ------------------------------------------
# Two-word combinations
# ------------------------------------------

if use_two_words:

    print("Generating 2-word combinations...")

    for a in variations:

        for b in variations:

            if a == b:
                continue

            for separator in separators:

                base1 = a + separator + b
                base2 = b + separator + a

                result.add(base1)
                result.add(base2)

                # Numbers
                if use_numbers:

                    for number in numbers:

                        result.add(base1 + number)
                        result.add(number + base1)

                        result.add(base2 + number)
                        result.add(number + base2)

                # Special characters
                if use_special:

                    for special in specials:

                        result.add(base1 + special)
                        result.add(special + base1)

                        result.add(base2 + special)
                        result.add(special + base2)

                        if use_numbers:

                            result.add(
                                base1 + special + number
                            )

                            result.add(
                                base2 + special + number
                            )


# ------------------------------------------
# Three-word combinations
# ------------------------------------------

if use_three_words:

    print("Generating 3-word combinations...")

    for combo in itertools.permutations(words, 3):

        a, b, c = combo

        for separator in separators:

            base = (
                a
                + separator
                + b
                + separator
                + c
            )

            result.add(base)

            # Numbers
            if use_numbers:

                for number in numbers:

                    result.add(base + number)
                    result.add(number + base)

            # Special characters
            if use_special:

                for special in specials:

                    result.add(base + special)
                    result.add(special + base)

                    if use_numbers:

                        result.add(
                            base
                            + special
                            + number
                        )


# ------------------------------------------
# Save file
# ------------------------------------------

filename = input(
    "\nOutput filename [wordlist.txt]: "
).strip()

if not filename:
    filename = "wordlist.txt"


print("\nSaving wordlist...")

with open(
    filename,
    "w",
    encoding="utf-8"
) as file:

    for password in sorted(result):
        file.write(password + "\n")


# ------------------------------------------
# Finished
# ------------------------------------------

print("\n" + "=" * 50)
print("             COMPLETE")
print("=" * 50)

print("Output file :", filename)
print("Total words :", len(result))

print("=" * 50)
