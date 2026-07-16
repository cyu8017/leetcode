export function isDesignCase(testCase) {
  return testCase?.kind === "design";
}

export function usesDesignCases(casesDoc) {
  return (casesDoc.cases || []).some(isDesignCase);
}

function listToTree(values) {
  if (!values || values.length === 0) return null;
  const root = { val: values[0], left: null, right: null };
  const queue = [root];
  let i = 1;
  while (queue.length > 0 && i < values.length) {
    const node = queue.shift();
    if (i < values.length) {
      if (values[i] !== null && values[i] !== undefined) {
        node.left = { val: values[i], left: null, right: null };
        queue.push(node.left);
      }
      i += 1;
    }
    if (i < values.length) {
      if (values[i] !== null && values[i] !== undefined) {
        node.right = { val: values[i], left: null, right: null };
        queue.push(node.right);
      }
      i += 1;
    }
  }
  return root;
}

function designCallArgs(rawArgs) {
  if (rawArgs == null) return [];
  if (Array.isArray(rawArgs)) return rawArgs;
  return [rawArgs];
}

function deepEqual(actual, expected) {
  const normalizedActual = actual === undefined ? null : actual;
  const normalizedExpected = expected === undefined ? null : expected;
  if (Array.isArray(normalizedActual) && Array.isArray(normalizedExpected)) {
    if (normalizedActual.length !== normalizedExpected.length) {
      return false;
    }
    return normalizedActual.every((item, index) => deepEqual(item, normalizedExpected[index]));
  }
  if (typeof normalizedActual === "number" || typeof normalizedExpected === "number") {
    const actualNumber = Number(normalizedActual);
    const expectedNumber = Number(normalizedExpected);
    if (Number.isFinite(actualNumber) && Number.isFinite(expectedNumber)) {
      return Math.abs(actualNumber - expectedNumber) < 1e-5;
    }
  }
  return JSON.stringify(normalizedActual) === JSON.stringify(normalizedExpected);
}

function listIterator(values) {
  let index = 0;
  return {
    next() {
      const value = values[index];
      index += 1;
      return value;
    },
    hasNext() {
      return index < values.length;
    },
  };
}

function jsonToNestedInteger(value) {
  if (typeof value === "number") {
    return {
      isInteger() {
        return true;
      },
      getInteger() {
        return value;
      },
      getList() {
        return [];
      },
    };
  }
  const list = value.map((entry) => jsonToNestedInteger(entry));
  return {
    isInteger() {
      return false;
    },
    getInteger() {
      return 0;
    },
    getList() {
      return list;
    },
  };
}

function jsonToNestedList(values) {
  return values.map((value) => jsonToNestedInteger(value));
}

function resolveDesignClass(exported, className) {
  if (typeof exported[className] === "function") {
    return exported[className];
  }
  if (exported.default && exported.default.name === className) {
    return exported.default;
  }
  if (exported.Solution && exported.Solution.name === className) {
    return exported.Solution;
  }
  throw new Error(`Design class ${className} not found in solution module`);
}

export function runDesignCase(exported, testCase) {
  const { operations, arguments: argLists, expected } = testCase;
  let instance = null;
  const actualOutputs = [];

  const uniformSequence = testCase.randomUniformSequence;
  if (uniformSequence != null) {
    let sequenceIndex = 0;
    const mockUniform = () => {
      if (sequenceIndex >= uniformSequence.length) {
        throw new Error("randomUniformSequence exhausted");
      }
      const value = uniformSequence[sequenceIndex];
      sequenceIndex += 1;
      return value;
    };
    if (typeof exported.set_uniform === "function") {
      exported.set_uniform(mockUniform);
    } else if (typeof exported.setUniform === "function") {
      exported.setUniform(mockUniform);
    } else {
      exported.uniform = mockUniform;
    }
  }

  for (let index = 0; index < operations.length; index += 1) {
    const operation = operations[index];
    const callArgs = designCallArgs(argLists[index]);
    let result;

    if (index === 0) {
      const Cls = resolveDesignClass(exported, operation);
      if (operation === "BSTIterator" && callArgs.length > 0 && Array.isArray(callArgs[0])) {
        callArgs[0] = listToTree(callArgs[0]);
      }
      if (operation === "PeekingIterator" && callArgs.length > 0 && Array.isArray(callArgs[0])) {
        callArgs[0] = listIterator(callArgs[0]);
      }
      if (operation === "NestedIterator" && callArgs.length > 0 && Array.isArray(callArgs[0])) {
        callArgs[0] = jsonToNestedList(callArgs[0]);
      }
      instance = new Cls(...callArgs);
      result = null;
    } else {
      if (!instance) {
        throw new Error(`Design case missing constructor before operation ${operation}`);
      }
      result = instance[operation](...callArgs);
    }

    actualOutputs.push(result);
    if (!deepEqual(result, expected[index])) {
      return { ok: false, actualOutputs, expected, step: index };
    }
  }

  return { ok: true, actualOutputs, expected, step: operations.length - 1 };
}

export function runDesignCases(exported, casesDoc) {
  let passed = 0;
  const total = casesDoc.cases?.length || 0;

  casesDoc.cases.forEach((testCase, index) => {
    if (!isDesignCase(testCase)) {
      console.log(`  SKIP case ${index + 1}: expected kind=design`);
      return;
    }

    try {
      const result = runDesignCase(exported, testCase);
      if (result.ok) {
        passed += 1;
        console.log(`  PASS case ${index + 1}`);
      } else {
        console.log(
          `  FAIL case ${index + 1} step ${result.step + 1}: expected ${JSON.stringify(result.expected[result.step])}, got ${JSON.stringify(result.actualOutputs[result.step])}`,
        );
      }
    } catch (error) {
      console.log(`  FAIL case ${index + 1}: ${error.message}`);
    }
  });

  return { passed, total };
}
