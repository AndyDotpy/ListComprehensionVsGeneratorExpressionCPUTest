from os import times
from _io import TextIOWrapper


tests_num: int = 1
seperator_left: str = ("#" * 10) + " " + ('-' * 10) + " " + ("_" * 7) + " " + ("|" * 4)
seperator_right: str = seperator_left[::-1]


def run_test(repetitions: int, elements: int, output_file: TextIOWrapper) -> None:
    global tests_num, seperator_left, seperator_right

    sys_start: float
    sys_end: float
    sys_dif: float
    user_start: float
    user_end: float
    user_dif: float

    generator_sys_total: float = 0.0
    generator_user_total: float = 0.0
    list_sys_total: float = 0.0
    list_user_total: float = 0.0

    start_time: times
    end_time: times

    print(
        seperator_left + f"Test {tests_num}" + seperator_right + "\n",
        f"Elements: {elements}\n",
        file=output_file
    )

    for repetition in range(repetitions):
        start_time = times()
        sys_start, user_start = start_time.system, start_time.user
        sum(v for v in range(elements))
        end_time = times()
        sys_end, user_end = end_time.system, end_time.user

        sys_dif, user_dif = sys_end - sys_start, user_end - user_start
        generator_sys_total += sys_dif
        generator_user_total += user_dif

        print(
            f"(Genr) - Repetition: {repetition}, total time: {sys_dif + user_dif}, system time: {sys_dif}, user time {user_dif}",
            file=output_file
        )

        start_time = times()
        sys_start, user_start = start_time.system, start_time.user
        sum([v for v in range(elements)])
        end_time = times()
        sys_end, user_end = end_time.system, end_time.user

        sys_dif, user_dif = sys_end - sys_start, user_end - user_start
        list_sys_total += sys_dif
        list_user_total += user_dif

        print(
            f"(List) - Repetition: {repetition}, total time: {sys_dif + user_dif}, system time: {sys_dif}, user time {user_dif}",
            file=output_file
        )


    print(
        f"(Generator Expression)\n",
        f"Total time: {generator_sys_total + generator_user_total}\n",
        f"Total system time: {generator_sys_total}\n",
        f"Total user time: {generator_user_total}\n",
        f"Time average per repetition: {(generator_sys_total + generator_user_total) / repetitions}\n",
        f"System time average per repetition: {generator_sys_total / repetitions}\n",
        f"User time average per repetition: {generator_user_total / repetitions}\n",
        f"(List Comprehension)\n",
        f"Total time: {list_sys_total + list_user_total}\n",
        f"Total system time: {list_sys_total}\n",
        f"Total user time: {list_user_total}\n",
        f"Time average per repetition: {(list_sys_total + list_user_total) / repetitions}\n",
        f"System time average per repetition: {list_sys_total / repetitions}\n",
        f"User time average per repetition: {list_user_total / repetitions}\n",
        seperator_left + f"End of test {tests_num}" + seperator_right,
        file=output_file
    )
    tests_num += 1


def main() -> None:
    while True:
        try:
            output_file: TextIOWrapper = open(input("Enter file path for results to be stored: "), "w")
            break
        except OSError as e:
            print(f"Failed to open file due to {e}")

    elements: int = 1000
    while elements <= 10000000:
        run_test(
            repetitions=20,
            elements=elements,
            output_file=output_file
        )
        elements *= 10

    output_file.flush()
    output_file.close()



if __name__ == "__main__":
    main()
