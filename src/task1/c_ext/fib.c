#include <Python.h>

int fib(int n){
  return (n>1) ? fib(n-1) + fib(n-2) : n;
}

static PyObject* fib_count(PyObject* self, PyObject* args) {
  int n = 2;
  PyArg_ParseTuple(args, "i", &n);
  return Py_BuildValue("i", fib(n));
}

static PyMethodDef fib_count_funcs[] = {
  {"fib_count",
   (PyCFunction)fib_count,
   METH_VARARGS,
   "Counts fibonacci n'th element"},
   {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
  PyModuleDef_HEAD_INIT,
  "fib_count_c",
  NULL,
  -1,
  fib_count_funcs
};

PyMODINIT_FUNC  PyInit_fib_count_c(void) {
  return PyModule_Create(&moduledef);
}