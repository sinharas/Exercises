def sum_array(num_list):
  if not list:
      return 0
  return num_list[0] + sum_array(num_list[1:])