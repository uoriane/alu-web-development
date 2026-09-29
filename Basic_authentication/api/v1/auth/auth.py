def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False if path is in excluded_paths (slash tolerant),
            True otherwise.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        # Normalize path to ensure slash tolerance
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            normalized_excluded = (
                excluded_path if excluded_path.endswith('/')
                else excluded_path + '/'
            )
            if normalized_path == normalized_excluded:
                return False

        return True
