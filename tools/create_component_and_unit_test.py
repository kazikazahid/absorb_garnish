#!/usr/bin/env python
import os
import sys


def print_usage_and_exit():
    print("usage : " + __file__ + " COMPONENT")
    print("Creates the .hpp, .cpp, and *_test.cpp files and build rules for a unit test.")
    sys.exit(1)

if len(sys.argv) < 2:
    print_usage_and_exit()

def main():
    component = sys.argv[1]
    file_extensions_to_create = ['.hpp', '.cpp', '_test.cpp']

    # Ensure components don't already exist
    for ext in file_extensions_to_create:
        if os.path.exists(os.path.join(os.getcwd(), component + ext)):
            print("CANNOT CREATE COMPONENT + UNIT TEST: {} already exists.".format(ext))
            sys.exit(1)

    # Prevent overriding our BUILD file.
    if not os.path.exists(os.path.join(os.getcwd(), 'BUILD')):
        build_file_mode = 'w'
    else:
        build_file_mode = 'a'

    with open(os.path.join(os.getcwd(), 'BUILD'), build_file_mode) as build_file:
        # Adds our unit test.
        if build_file_mode == 'w':
            print >>build_file, "load('//tools:gtest.bzl', 'gtest_unit')"
        print >>build_file, "gtest_unit(name='{}')".format(component)

    # ...
    # Race condition here... assume people are nice and doesn't happen.
    # ...

    # TODO: Might not have adequate permissions.
    with open(component + ".hpp", "w") as f:
        print >>f, "#pragma once"

    with open(component + ".cpp", "w") as f:
        print >>f, "#include \"{}.hpp\"".format(component)

    with open(component + "_test.cpp", "w") as f:
        contents = """
#include <gtest/gtest.h>

#include "{}.hpp"

/* Basic GoogleTest operations.
Basic Test:
TEST(test_name, case_name) {{
}}

Test from Fixture:
TEST_F(fixture_name, test_name) {{
}}

class A_Fixture_Class : public ::testing::Test {{
protected:
    virtual void SetUp() {{}}
    virtual void TearDown() {{}}

// Only do one SetUp/TearDown for all tests by using SetUpTestCase and
// TearDownTestCase instead.
}}

Assertions:
for non-fatal use EXPECT_*
ASSERT_TRUE, ASSERT_FALSE
ASSERT_EQ(val1,val2)
similarly, NE (!=), LT (<), LE (<=), GT (>), GE (>=)

Floating point:
ASSERT_FLOAT_EQ, ASSERT_DOUBLE_EQ
ASSERT_NEAR(a, b, abs_error)

C-string comparisons:
ASSERT_STREQ(str1,str2)
similarly: STRNE, STRCASEEQ, STRCASENE

SUCCEED - guarantee success
FAIL - fatal failure
ADD_FAILURE, ADD_FAILIURE_AT - non-fatal failures (like EXPECT)

ASSERT_THROW(stmt, exception)
ASSERT_ANY_THROW(stmt), ASSERT_ON_THROW(stmt)

ASSERT_PRED1(predicate, value), ASSERT_PRED2(predicate, value1, value2)

Tracing Assertions:
SCOPED_TRACE(message)
*/


// Boilerplate
int main(int argc, char * argv[])
{{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}}
    """.format(component)
        print >>f, contents

if __name__ == '__main__':
    main()
