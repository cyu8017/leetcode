# LeetCode 0588 - Design In-Memory File System
# https://leetcode.com/problems/design-in-memory-file-system/

from typing import List


class FileSystem:
    def __init__(self):
        # Directories are dicts; files are strings (content).
        self.root: dict = {}

    def _parts(self, path: str) -> list[str]:
        return [part for part in path.split("/") if part]

    def ls(self, path: str) -> List[str]:
        if path == "/":
            return sorted(self.root.keys())

        parts = self._parts(path)
        node: dict | str = self.root
        for part in parts:
            node = node[part]  # type: ignore[index]

        if isinstance(node, str):
            return [parts[-1]]
        return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        node = self.root
        for part in self._parts(path):
            node = node.setdefault(part, {})

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = self._parts(filePath)
        node = self.root
        for part in parts[:-1]:
            next_node = node.setdefault(part, {})
            if isinstance(next_node, str):
                raise ValueError("Path conflict")
            node = next_node

        name = parts[-1]
        existing = node.get(name, "")
        if isinstance(existing, dict):
            raise ValueError("Path conflict")
        node[name] = existing + content

    def readContentFromFile(self, filePath: str) -> str:
        parts = self._parts(filePath)
        node: dict | str = self.root
        for part in parts:
            node = node[part]  # type: ignore[index]
        return node  # type: ignore[return-value]
