def gtest_unit(name,
               components=[],
               srcs=[],
               deps=[], 
               copts=[],
               size="small",
               args=[],
              **kwargs):
  """Creates a unit test for a component (hpp/cpp pair)."""
  # Build list of components (.hpp and .cpp components)
  components = components + [name]
  for x in components:
    srcs = srcs + [x + ".hpp", x + ".cpp"]

  native.cc_test(
    name = name + "_test",
    deps = deps + ["@gtest//:lib"],
    srcs = srcs + [name + "_test.cpp"],
    copts = copts + ["-Wall", "-Wextra", "-Werror", "-Iexternal/gtest/include", "-std=c++14"],
    size = size,

    # Ensure we get colorized output from bazel.
    args = args + ["--gtest_color=yes"],

    # Pass the rest of the args.
    **kwargs
  )
