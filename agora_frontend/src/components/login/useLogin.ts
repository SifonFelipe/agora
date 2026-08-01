import { useState } from "react";
import type { LoginCredentials, LoginResponse, LoginError } from "./loginTypes";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export function useLogin() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const login = async (credentials: LoginCredentials): Promise<boolean> => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE_URL}/auth/login/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(credentials),
      });

      if (!response.ok) {
        const errorData: LoginError = await response.json();
        setError(errorData.detail ?? "Credenciales inválidas");
        return false;
      }

      const data: LoginResponse = await response.json();
      localStorage.setItem("access_token", data.access);
      localStorage.setItem("refresh_token", data.refresh);
      return true;
    } catch (err) {
      setError("No se pudo conectar con el servidor");
      return false;
    } finally {
      setIsLoading(false);
    }
  };

  return { login, isLoading, error };
}
