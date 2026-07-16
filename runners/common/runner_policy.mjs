/** Shared exit-code policy for JavaScript/TypeScript test runners. */

export const EXIT = {
  OK: 0,
  FAIL: 1,
  CONFIG: 2,
  NO_CASES: 4,
};

const DESIGN_NATIVE = new Set(["python", "javascript", "typescript", "java"]);
const COMPILED = new Set(["cpp", "c", "go", "rust", "kotlin", "csharp", "scala", "swift"]);
const UNSUPPORTED_KINDS = new Set(["sql", "shell", "pandas"]);

export function resolveKind(config, casesDoc) {
  if (config.kind) return config.kind;
  const cases = casesDoc.cases || [];
  if (cases.length && cases[0].kind) return cases[0].kind;
  return "standard";
}

export function preRunCheck(language, config, casesDoc, options = {}) {
  const {
    hasSolutionFile = true,
    hasPythonReference = false,
    toolchainAvailable = true,
  } = options;
  const cases = casesDoc.cases || [];
  if (!cases.length) {
    return { canRun: false, exitCode: EXIT.NO_CASES, message: "no test cases defined in tests/cases.json" };
  }

  const kind = resolveKind(config, casesDoc);
  if (UNSUPPORTED_KINDS.has(kind)) {
    if (config.runnable === false) {
      return { canRun: false, exitCode: EXIT.OK, message: `SKIP kind=${kind} (runner not implemented)` };
    }
    return { canRun: false, exitCode: EXIT.CONFIG, message: `kind=${kind} requires a runner but none is configured` };
  }

  if (kind === "design") {
    if (DESIGN_NATIVE.has(language)) {
      if (!hasSolutionFile) {
        return { canRun: false, exitCode: EXIT.CONFIG, message: `missing solution file for ${language}` };
      }
      if (!toolchainAvailable) {
        return { canRun: false, exitCode: EXIT.CONFIG, message: `${language} toolchain not available` };
      }
      return { canRun: true, exitCode: EXIT.OK, message: "" };
    }
    if (COMPILED.has(language)) {
      if (!hasPythonReference) {
        return {
          canRun: false,
          exitCode: EXIT.CONFIG,
          message: "design problems require a Python reference implementation",
        };
      }
      return { canRun: true, exitCode: EXIT.OK, message: "" };
    }
    return {
      canRun: false,
      exitCode: EXIT.CONFIG,
      message: `design cases not supported for language=${language}`,
    };
  }

  if (!hasSolutionFile) {
    return { canRun: false, exitCode: EXIT.CONFIG, message: `missing solution file for ${language}` };
  }
  if (!toolchainAvailable) {
    return { canRun: false, exitCode: EXIT.CONFIG, message: `${language} toolchain not available` };
  }
  return { canRun: true, exitCode: EXIT.OK, message: "" };
}
