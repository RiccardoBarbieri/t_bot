import sys
sys.path.append('C:\\Users\\ricca\\Desktop\\telegram')
from parsers.parsing_curricula_codes import create_curriculas_with_codes
from parsers.joining_curriculas_courses import join
from parsers.crafting_correct_links import correct_links
from parsers.parsing_courses import CourseParser
import json


if __name__ == '__main__':
    parser = CourseParser()

    with open('courses.json', 'w+') as f:
        json.dump(parser.get_parsed_cards(), f)
    
    correct_links()

    create_curriculas_with_codes()

    join()
