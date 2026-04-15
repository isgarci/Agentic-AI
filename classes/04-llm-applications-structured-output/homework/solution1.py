import json
import os
from openai import OpenAI
from typing import Literal, Callable
from dotenv import load_dotenv
from colorama import Fore, Back, Style, init

init(autoreset=True)
load_dotenv()


def classify_sentiment(review: str) -> Literal["Positive", "Neutral", "Negative"]:
    client = OpenAI(
        api_key=os.environ.get("GROQ_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    prompt = f"""
        You are an expert tasked with classifying review into the following categories: ["Positive", "Neutral", "Negative"].
        Below is the input review:
        REVIEW BEGIN
        {review}
        REVIEW END
        Output just a single word.
        """
    response = client.responses.create(
        input=prompt, model="openai/gpt-oss-20b", temperature=1.9999
    )
    return response.output_text


def classify_email(
    e_mail: str,
) -> Literal[
    "Sales and Pre-Sales", "IT Support", "Returns and Exchanges", "Human Resources"
]:
    client = OpenAI(
        api_key=os.environ.get("GROQ_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    prompt = f"""
        You are an expert tasked with classifying an e-mail that a company receives into the following categories:
         - "Sales and Pre-Sales",
         - "IT Support",
         - "Returns and Exchanges",
         - "Human Resources"
        Below is the input e-mail:
        EMAIL BEGIN
        {e_mail}
        EMAIL END
        Output just the name of the category.
        """
    response = client.responses.create(
        input=prompt, model="openai/gpt-oss-20b", temperature=1.9999
    )
    return response.output_text


def filter_message(input_message: str) -> Literal["allowed", "filtered"]:
    client = OpenAI(
        api_key=os.environ.get("GROQ_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    prompt = f"""
        You are an expert tasked with classifying a message sent in an online in-game chat as either "allowed" or "filtered".
        Below is the message e-mail:
        EMAIL BEGIN
        {input_message}
        EMAIL END
        Output just the word "allowed" or "filtered".
        """
    response = client.responses.create(
        input=prompt, model="openai/gpt-oss-20b", temperature=1.9999
    )
    return response.output_text


def test_scaffold(method_to_test: Callable, test_set: dict):
    print(f"{Fore.CYAN}{'=' * 60}")
    print(f"{Fore.CYAN}Testing: {Fore.YELLOW}{method_to_test.__name__}")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    counter = 0
    incorrect = []
    for value in test_set:
        predicted_label = method_to_test(value["Text"])
        actual_label = value["Label"]
        if predicted_label.lower() != actual_label.lower():
            incorrect.append(
                {
                    "Text": value["Text"],
                    "True Label": actual_label,
                    "Prediction": predicted_label,
                }
            )
        counter += 1
        if counter == 10:
            break

    # Print results
    total_tests = counter
    correct = total_tests - len(incorrect)
    accuracy = (correct / total_tests) * 100 if total_tests > 0 else 0

    print(f"\n{Fore.CYAN}{'─' * 60}")
    print(f"{Fore.CYAN}Results Summary:")
    print(f"{Fore.CYAN}{'─' * 60}")
    print(f"{Fore.WHITE}Total Tests: {Fore.YELLOW}{total_tests}")
    print(f"{Fore.GREEN}Correct: {correct}")
    print(f"{Fore.RED}Incorrect: {len(incorrect)}")
    print(f"{Fore.MAGENTA}Accuracy: {accuracy:.1f}%")

    if incorrect:
        print(f"\n{Fore.RED}{'=' * 60}")
        print(f"{Fore.RED}Failed Test Cases ({len(incorrect)} mistakes):")
        print(f"{Fore.RED}{'=' * 60}{Style.RESET_ALL}")

        for i, mistake in enumerate(incorrect, 1):
            print(f"\n{Fore.YELLOW}[Mistake #{i}]")
            print(f"{Fore.WHITE}Text: {Fore.CYAN}{mistake['Text']}")
            print(f"{Fore.WHITE}Expected: {Fore.GREEN}{mistake['True Label']}")
            print(f"{Fore.WHITE}Got:      {Fore.RED}{mistake['Prediction']}")
            if i < len(incorrect):
                print(f"{Fore.WHITE}{'-' * 60}")
    else:
        print(f"\n{Back.GREEN}{Fore.BLACK} ✓ ALL TESTS PASSED! {Style.RESET_ALL}")

    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}\n")


if __name__ == "__main__":
    directory = os.path.dirname(__file__)

    print(f"\n{Back.BLUE}{Fore.WHITE} Starting Test Suite {Style.RESET_ALL}\n")

    test1 = None
    with open(directory + "/test1.json") as f:
        test1 = json.load(f)
        test_scaffold(classify_sentiment, test1)

    with open(directory + "/test2.json") as f:
        test2 = json.load(f)
        test_scaffold(classify_email, test2)

    with open(directory + "/test3.json") as f:
        test3 = json.load(f)
        test_scaffold(filter_message, test3)

    print(f"{Back.BLUE}{Fore.WHITE} Test Suite Complete {Style.RESET_ALL}\n")
